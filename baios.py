import logging
import asyncio
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.util.task import TaskState
from agent_storyline import StorylineAgent

# --- Basic Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Baios:
    """
    An orchestrator that encapsulates a SpiffWorkflow BpmnWorkflow instance
    and drives its execution by handling ready tasks.
    """
    def __init__(self, process):
        """
        Initializes the orchestrator with a workflow specification.

        Args:
            process: The parsed BPMN workflow specification.
        """
        self.workflow = BpmnWorkflow(process)

    async def _run_scheduler(self):
        """
        The private scheduler loop that polls for ready tasks and dispatches
        them to the correct agent or logic.
        """
        ready_tasks = self.workflow.get_tasks(state=TaskState.READY)
        while ready_tasks:
            for task in ready_tasks:
                if task.task_spec.name == 'TaskStoryLine':
                    logging.info(f"Executing task: '{task.task_spec.name}'")
                    
                    # --- Agent Logic ---
                    agent = StorylineAgent()
                    try:
                        result = await agent.generate()
                        task.set_data(storyline_result=result)
                    except Exception as e:
                        logging.error(f"Agent execution failed: {e}", exc_info=True)
                        task.set_data(storyline_error=str(e))
                    # -------------------

                    task.complete()
                    logging.info(f"Task '{task.task_spec.name}' completed.")
                    
                    # Run the workflow again to process the completion
                    self.workflow.run_all()
            
            ready_tasks = self.workflow.get_tasks(state=TaskState.READY)

    def run_all(self):
        """A synchronous wrapper that runs the entire async workflow."""
        return asyncio.run(self.run())

    async def run(self):
        """
        This is the main execution loop that prepares the workflow and
        starts the scheduler.
        """
        logging.info("Starting baiOS workflow execution...")
        
        # First, run to the first ready task
        self.workflow.run_all() 

        # Await all task executions
        await self._run_scheduler()

        logging.info("Workflow finished.")
        return self.workflow.data

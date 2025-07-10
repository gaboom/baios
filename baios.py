import os
import logging
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.bpmn.parser import BpmnValidator
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser

# --- Basic Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# =================================================================
# GENERIC BAIOS ORCHESTRATOR
# =================================================================
def main():
    """
    This is a generic orchestrator. It loads and runs a BPMN file,
    assuming the file itself contains all necessary script logic.
    """
    # 1. Create the BPMN parser and load the file.
    parser = SpiffBpmnParser(validator=BpmnValidator())
    parser.add_bpmn_file('POC-GAME_GENERATOR.bpmn')
    spec = parser.get_spec('GamePocGenerator')

    # 2. Create and run the workflow.
    #    No specific task logic is needed here.
    workflow = BpmnWorkflow(spec)
    logging.info("Starting baiOS workflow...")
    workflow.run_all()
    logging.info("Workflow finished.")

    # 3. Print the final context from the workflow.
    print("\n" + "="*20 + " FINAL CONTEXT " + "="*20)
    if "storyline_result" in workflow.data:
        print("Generated Storyline:")
        print(workflow.data["storyline_result"])
    if "storyline_error" in workflow.data:
        print("Error:")
        print(workflow.data["storyline_error"])
    print("="*55)


if __name__ == "__main__":
    main()
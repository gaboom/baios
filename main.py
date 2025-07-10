import os
import argparse
from SpiffWorkflow.bpmn.parser import BpmnValidator
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser
from baios import Baios

def get_workflow_spec(bpmn_file_path, process_id=None):
    """
    Loads and parses the BPMN file to get a specific process spec.
    If process_id is not provided, it defaults to the base name of the
    BPMN file without its extension.
    """
    if process_id is None:
        process_id = os.path.splitext(os.path.basename(bpmn_file_path))[0]
    
    parser = SpiffBpmnParser(validator=BpmnValidator())
    parser.add_bpmn_file(bpmn_file_path)
    return parser.get_spec(process_id)

def boot(bpmn_file_path, verbose=False):
    """
    Boots up the BAIOS system.
    1. Loads the workflow definition.
    2. Instantiates the custom orchestrator class.
    3. Runs the workflow.
    """
    boot_spec = get_workflow_spec(bpmn_file_path)
    orchestrator = Baios(boot_spec)
    workflow_data = orchestrator.run_all()
    
    if verbose:
        print("\n" + "="*20 + " FINAL CONTEXT " + "="*20)
        print("Workflow data:", workflow_data)
        print("="*55)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BAI-OS Workflow Orchestrator")
    default_workflow = os.path.join(os.path.dirname(__file__), 'WorkflowGameGenerator.bpmn')
    
    parser.add_argument(
        "-w", "--workflow", "-i", "--bpmn",
        dest="bpmn_file",
        default=default_workflow,
        help=f"Path to the BPMN workflow file (default: {default_workflow})"
    )
    parser.add_argument(
        "-v", "--verbose", "-o",
        action="store_true",
        help="Print the final workflow data context upon completion."
    )
    
    args = parser.parse_args()
    boot(args.bpmn_file, args.verbose)

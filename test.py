"""
Main entry point for the DialogStream.
"""

import click
import logging
import signal
import sys
from dialogstream import StreamFilterRouter, ManagedProcess

def signal_handler(signum, frame):
    """Handle shutdown signal by setting the global exit flag"""
    sys.exit(0)

@click.command()
@click.option('--flows-config', '-s', 
              default="config/flows.json",
              help="Path to flows configuration JSON file",
              type=click.Path(exists=True))
@click.option('--process-config', '-p',
              default="config/process.json",
              help="Path to process configuration JSON file",
              type=click.Path(exists=True))
def main(flows_config: str, process_config: str):
    """Main entry point for the DialogStream."""
    
    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    router = StreamFilterRouter(flows_config, process_config)

    try:
        router.start()
        # Use signal.pause() instead of infinite loop
        signal.pause()
    except (KeyboardInterrupt, SystemExit):
        router.stop()
        logging.info("DialogStream shutdown complete")
        sys.exit(0)

if __name__ == "__main__":
    main()

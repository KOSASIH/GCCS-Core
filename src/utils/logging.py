# src/utils/logging.py

import logging
import os

def setup_logging(log_file='app.log', log_level=logging.INFO):
    """Set up logging configuration."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=log_level
    )
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    
    logging.getLogger().addHandler(console_handler)

if __name__ == "__main__":
    setup_logging()
    logging.info("Logging setup complete.")

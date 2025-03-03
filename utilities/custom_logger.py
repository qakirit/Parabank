import logging
import os


class LogMaker:
    @staticmethod
    def log_gen():
        """Generate a logger instance for test reporting."""
        # Ensure the Logs directory exists
        log_dir = "C:\\Users\\kirit\\PycharmProjects\\ParaBank Banking\\Logs\\parabank"
        os.makedirs(log_dir, exist_ok=True)

        # Logger instance
        logger = logging.getLogger("ParababjLogger")

        logger.setLevel(logging.DEBUG)
        #logger.setLevel(logging.info("Bank logger"))

        # Avoid duplicate handlers
        if not logger.handlers:
            # File Handler
            file_handler = logging.FileHandler(os.path.join(log_dir, "bank.log"))
            file_handler.setLevel(logging.DEBUG)
            file_formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)

        return logger

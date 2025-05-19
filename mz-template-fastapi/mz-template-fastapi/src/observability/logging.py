import logging
import json
from logging import Formatter, LogRecord
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

class JsonFormatter(Formatter):
    def __init__(self, datefmt: str = "%Y-%m-%d %H:%M:%S"):
        super().__init__()
        self.datefmt = datefmt  # Ensure datefmt is initialized

    def format(self, record: LogRecord) -> str:
        try:
            log_record = {
                "level": record.levelname,
                "message": record.getMessage(),
                "time": self.formatTime(record, self.datefmt),
                "name": record.name,
                "filename": record.filename,
                "lineno": record.lineno,
            }
            return json.dumps(log_record)
        except Exception as e:
            return json.dumps({"error": f"Failed to format log record: {str(e)}"})

def setup_logging() -> None:
    logger = logging.getLogger(__name__)
    if not logger.handlers:  # Prevent duplicate handlers
        log_handler = logging.StreamHandler()
        formatter = JsonFormatter()
        log_handler.setFormatter(formatter)

        logger.setLevel(logging.INFO)
        logger.addHandler(log_handler)

    # Setup OpenTelemetry Tracing
    resource = Resource(attributes={"service.name": "your-service-name"})
    tracer_provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(tracer_provider)

    span_processor = BatchSpanProcessor(ConsoleSpanExporter())
    tracer_provider.add_span_processor(span_processor)

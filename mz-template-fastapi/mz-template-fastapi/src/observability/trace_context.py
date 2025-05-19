from contextvars import ContextVar
trace_id_var = ContextVar("trace_id", default=None)
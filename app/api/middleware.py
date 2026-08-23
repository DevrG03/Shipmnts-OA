import logging
import time
import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger("app.middleware")


class RequestLoggingAndTimingMiddleware(BaseHTTPMiddleware):
    """Attaches a unique X-Request-ID and tracks latency via X-Process-Time-Ms."""

    async def dispatch(self, request: Request, call_next) -> Response:
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        request.state.request_id = request_id

        start_time = time.perf_counter()
        response: Response = await call_next(request)
        process_time_ms = (time.perf_counter() - start_time) * 1000

        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time-Ms"] = f"{process_time_ms:.2f}"

        logger.info(
            "%s %s - status: %s - took: %.2fms [req_id=%s]",
            request.method,
            request.url.path,
            response.status_code,
            process_time_ms,
            request_id,
        )
        return response

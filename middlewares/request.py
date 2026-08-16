# Libs
from fastapi import Request  # FastAPI
from starlette.middleware.base import BaseHTTPMiddleware  # Starlette
from starlette.responses import Response  # Starlette
import time  # Time
import uuid  # UUID

# Application
from core.database import session  # Database: Session
from models.request import Request as RequestLog  # Model: Request


# The Request Middleware
class RequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request: Request,
        call_next,
    ) -> Response:
        start_time = time.perf_counter()

        request_id_header = request.headers.get("X-Request-ID")

        try:
            request_id = (
                uuid.UUID(request_id_header) if request_id_header else uuid.uuid4()
            )
        except ValueError:
            request_id = uuid.uuid4()

        method = request.method
        endpoint = request.url.path

        ip_address = request.client.host if request.client else None

        user_agent = request.headers.get("User-Agent")
        client_id = request.headers.get("X-Client-ID")

        request.state.request_id = request_id

        status_code = 500
        error = None

        try:
            response = await call_next(request)

            status_code = response.status_code

            return response

        except Exception as exc:
            error = f"{type(exc).__name__}: {exc}"

            raise

        finally:
            response_time = (time.perf_counter() - start_time) * 1000

            db = session()

            try:
                log = RequestLog(
                    request_id=request_id,
                    method=method,
                    endpoint=endpoint,
                    ip_address=ip_address,
                    user_agent=user_agent,
                    client_id=client_id,
                    status_code=status_code,
                    response_time=response_time,
                    error=error,
                )

                db.add(log)
                db.commit()

            except Exception:
                db.rollback()

            finally:
                db.close()

            if "response" in locals():
                response.headers["X-Request-ID"] = str(request_id)

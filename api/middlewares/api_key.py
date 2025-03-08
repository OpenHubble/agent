from fastapi import HTTPException, Request, Depends
from fastapi.security import HTTPBearer

import api.config.config as config

# Dependency function to check API key
def api_key(request: Request):
    api_key = request.headers.get("X-API-KEY")  # Get API key from request header

    # Compare with the stored API key (either from config or environment variable)
    if api_key != config.API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Forbidden: Invalid API key"
        )

from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_current_user
from app.models.auth import LoginRequest, SignUpRequest, TokenResponse, UserOut
from app.services.auth_service import auth_service

router = APIRouter()


@router.post("/signup", response_model=TokenResponse)
async def signup(request: SignUpRequest):
    try:
        result = auth_service.sign_up(request.email, request.password)
        session = result.session
        user = result.user
        if not session:
            raise HTTPException(
                status_code=200,
                detail="Check your email to confirm your account",
            )
        return TokenResponse(
            access_token=session.access_token,
            refresh_token=session.refresh_token,
            user=UserOut(
                id=str(user.id),
                email=user.email,
                created_at=user.created_at,
            ),
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    try:
        result = auth_service.sign_in(request.email, request.password)
        session = result.session
        user = result.user
        return TokenResponse(
            access_token=session.access_token,
            refresh_token=session.refresh_token,
            user=UserOut(
                id=str(user.id),
                email=user.email,
                created_at=user.created_at,
            ),
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.post("/logout")
async def logout(_=Depends(get_current_user)):
    auth_service.sign_out()
    return {"message": "Logged out"}


@router.get("/me", response_model=UserOut)
async def get_me(current_user=Depends(get_current_user)):
    return UserOut(
        id=str(current_user.id),
        email=current_user.email,
        created_at=current_user.created_at,
    )

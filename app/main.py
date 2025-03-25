from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, utils, database

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/wallet/", response_model=schemas.WalletData)
async def get_wallet_info(
    request: schemas.WalletRequestCreate, 
    db: Session = Depends(get_db)
):
    try:
        wallet_data = utils.get_tron_wallet_info(request.wallet_address)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    db_request = models.WalletRequest(wallet_address=request.wallet_address)
    db.add(db_request)
    db.commit()

    return {**wallet_data, "address": request.wallet_address}


@app.get("/requests/", response_model=list[schemas.WalletRequestOut])
async def get_requests(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.WalletRequest)\
             .order_by(models.WalletRequest.request_time.desc())\
             .offset(skip)\
             .limit(limit)\
             .all()

from datetime import datetime, timedelta
import json

from flask.testing import FlaskClient

from app import models as m, db
from tests.utils import login


def test_sale_reports(populate: FlaskClient):
    login(populate, email="test_user_17@gmail.com", password="123456")
    sale_rep = db.session.get(m.SaleReport, 1)
    gift_item = db.session.get(m.GiftItem, 1)
    user_gift_item = m.DealerGiftItem(
        dealer_id=sale_rep.label.user_id,
        gift_item_id=gift_item.id,
        min_qty=1,
        max_qty=3,
    ).save()
    assert sale_rep
    assert gift_item
    res = populate.get("/sale-reports", follow_redirects=True)
    assert res.status_code == 200
    assert f"{sale_rep.unique_id}" in res.data.decode()

    res = populate.get(f"/sale-reports/{sale_rep.unique_id}/gift-box-modal")
    assert res.status_code == 200
    assert f"{gift_item.description}" in res.data.decode()

    form_data = {
        "sale_rep_unique_id": sale_rep.unique_id,
        "phone": "123-456-7890",
        "first_name": "test",
        "last_name": "user",
        "password": "123456",
        "password_confirmation": "123456",
        "email": "b@b.com",
        "gift_boxes": json.dumps(
            [{"dealerGiftItemId": user_gift_item.id, "qty": 1, "totalPrice": 1}]
        ),
        "is_notfy_by_email": True,
    }
    assert not sale_rep.gift_boxes
    assert not sale_rep.buyer
    res = populate.post(
        "/sale-reports/set-gift-boxes", follow_redirects=True, data=form_data
    )
    assert res.status_code == 200
    db.session.add(
        m.OilChange(
            sale_rep_id=sale_rep.id,
            date=datetime.now() + timedelta(days=180),
        )
    )
    db.session.add(
        m.OilChange(
            sale_rep_id=sale_rep.id,
            date=datetime.now() + timedelta(days=360),
        )
    )
    db.session.commit()
    assert "Gift boxes added" in res.data.decode()

    assert sale_rep.buyer
    assert sale_rep.gift_boxes

    res = populate.get(f"/sale-reports/{sale_rep.unique_id}/buyer")
    assert res.status_code == 200
    assert sale_rep.buyer.email in res.data.decode()

    res = populate.get("/sale-reports/panding-oil")
    assert res.status_code == 200
    assert f"{sale_rep.unique_id}" in res.data.decode()

    res = populate.get(f"/sale-reports/{sale_rep.unique_id}/edit-modal")

    assert res.status_code == 200
    assert sale_rep.oil_changes[0].date.strftime("%d-%m-%Y") in res.data.decode()
    assert "b@b.com" in res.data.decode()

    form_data = {
        "unique_id": sale_rep.buyer.unique_id,
        "sale_rep_unique_id": sale_rep.unique_id,
        "phone": "123-456-7890",
        "first_name": "test",
        "last_name": "user",
        "email": "b2@b.com",
    }
    res = populate.post("/sale-reports/edit", follow_redirects=True, data=form_data)
    assert res.status_code == 200
    assert "Sale report updated" in res.data.decode()

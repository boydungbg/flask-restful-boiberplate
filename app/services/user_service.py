from sqlalchemy import or_, desc, asc
import math
from datetime import datetime
from flask import current_app
from app.helper.datatime import parser_datetime
from app.models.user import User
from app.services.base_service import save_change
from typing import List, Dict


def add_user(data: dict) -> bool:
    try:
        user = User(
            username=data["username"],
            email=data["email"],
            full_name=data["full_name"],
            password=data["password"],
        )
        save_change(user)
        return True
    except Exception as ex:
        current_app.logger.error(ex)
        return False


def get_user_by_id(id: int) -> User:
    try:
        user = User.query.where(User.id == id).first()
        return user
    except Exception as ex:
        current_app.logger.error(ex)
        return None


def get_list_user(data: dict) -> Dict:
    try:
        search = data.get("search")
        sort_by = data.get("sort_by")
        sort_type = data.get("sort_type")
        page = int(data.get("page"))
        per_page = int(data.get("per_page"))
        offset = (page - 1) * per_page
        # get query list user
        query = User.query
        if len(search) != 0:
            query = query.filter(_add_query_search(search))
        if data.get("status") != None:
            query = query.filter(User.status == int(data.get("status")))
        if data.get("created_at_min") != None and data.get("created_at_min") != None:
            query = query.filter(_add_query_datetime(data))
        query = query.order_by(_add_sort_by(sort_by, sort_type))
        query = query.offset(offset=offset).limit(limit=per_page)
        users = query.all()
        # end query list user
        count = _count_all_user(data)
        meta_data = {
            "count": count,
            "current_page": page,
            "per_page": per_page,
            "total_page": math.ceil(count / per_page),
        }
        return {"status": True, "data": users, "meta_data": meta_data}
    except Exception as ex:
        current_app.logger.error(ex)
        return {"status": False, data: []}


def is_email_exist(email: str) -> bool:
    try:
        count = User.query.filter_by(email=email).count()
        return count > 0
    except Exception as ex:
        current_app.logger.error(ex)
        return False


def is_username_exist(username: str) -> bool:
    try:
        count = User.query.filter_by(username=username).count()
        return count > 0
    except Exception as ex:
        current_app.logger.error(ex)
        return False


def _count_all_user(data: dict) -> int:
    search = data.get("search")
    query = User.query
    if len(search) != 0:
        query = query.filter(_add_query_search(search))
    if data.get("created_at_min") != None and data.get("created_at_min") != None:
        query = query.filter(_add_query_datetime(data))
    if data.get("status") != None:
        query = query.filter(User.status == int(data.get("status")))
    return query.count()


def _add_query_search(search: str):
    return or_(
        User.id == search,
        User.full_name.like(f"%{search}%"),
        User.username == search,
        User.email == search,
    )


def _add_query_datetime(data: dict) -> int:
    return User.created_at.between(data["created_at_min"], data["created_at_max"])


def _add_sort_by(sort_by: str, sort_type: str):
    if sort_type == "desc":
        return desc(sort_by)
    else:
        return asc(sort_by)

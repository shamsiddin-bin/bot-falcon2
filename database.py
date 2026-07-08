# database.py
"""
SQLite (aiosqlite) bilan ishlash uchun barcha async funksiyalar.

Jadvallar:
    users:          user_id, username, full_name, language, registered_at
    announcements:  id, text, file_id, file_type, created_at
    schedule:       id, file_id, file_type, caption, updated_at
    payments:       id, user_id, amount, transaction_id, status, created_at
"""

import aiosqlite
from datetime import datetime
from config import DATABASE_NAME


async def init_db() -> None:
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                full_name TEXT,
                language TEXT,
                registered_at TEXT
            )
            """
        )
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS announcements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                file_id TEXT,
                file_type TEXT,
                created_at TEXT
            )
            """
        )
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS schedule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id TEXT,
                file_type TEXT,
                caption TEXT,
                updated_at TEXT
            )
            """
        )
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                amount INTEGER,
                transaction_id TEXT,
                status TEXT,
                created_at TEXT
            )
            """
        )
        await db.commit()


# ==================== USERS ====================

async def add_user(user_id: int, username: str, full_name: str) -> None:
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute(
            """
            INSERT INTO users (user_id, username, full_name, registered_at)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                username = excluded.username,
                full_name = excluded.full_name
            """,
            (user_id, username, full_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        await db.commit()


async def get_user(user_id: int):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM users WHERE user_id = ?", (user_id,)
        ) as cursor:
            row = await cursor.fetchone()
            return dict(row) if row else None


async def set_user_language(user_id: int, language: str) -> None:
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute(
            "UPDATE users SET language = ? WHERE user_id = ?", (language, user_id)
        )
        await db.commit()


async def get_user_language(user_id: int) -> str | None:
    user = await get_user(user_id)
    return user["language"] if user else None


async def get_stats() -> dict:
    async with aiosqlite.connect(DATABASE_NAME) as db:
        stats = {}
        async with db.execute("SELECT COUNT(*) FROM users") as cur:
            stats["total"] = (await cur.fetchone())[0]
        for lang in ("uz", "ru", "en"):
            async with db.execute(
                "SELECT COUNT(*) FROM users WHERE language = ?", (lang,)
            ) as cur:
                stats[lang] = (await cur.fetchone())[0]
        return stats


async def get_recent_users(limit: int = 10) -> list:
    async with aiosqlite.connect(DATABASE_NAME) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM users ORDER BY registered_at DESC LIMIT ?", (limit,)
        ) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]


# ==================== ANNOUNCEMENTS ====================

async def add_announcement(text: str | None, file_id: str | None, file_type: str | None) -> None:
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute(
            """
            INSERT INTO announcements (text, file_id, file_type, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (text, file_id, file_type, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        await db.commit()


async def get_latest_announcement():
    async with aiosqlite.connect(DATABASE_NAME) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM announcements ORDER BY id DESC LIMIT 1"
        ) as cursor:
            row = await cursor.fetchone()
            return dict(row) if row else None


async def get_recent_announcements(limit: int = 5) -> list:
    async with aiosqlite.connect(DATABASE_NAME) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM announcements ORDER BY id DESC LIMIT ?", (limit,)
        ) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]


# ==================== SCHEDULE ====================

async def set_schedule(file_id: str, file_type: str, caption: str | None) -> None:
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute(
            """
            INSERT INTO schedule (file_id, file_type, caption, updated_at)
            VALUES (?, ?, ?, ?)
            """,
            (file_id, file_type, caption, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        await db.commit()


async def get_latest_schedule():
    async with aiosqlite.connect(DATABASE_NAME) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM schedule ORDER BY id DESC LIMIT 1"
        ) as cursor:
            row = await cursor.fetchone()
            return dict(row) if row else None


# ==================== PAYMENTS ====================

async def create_payment(user_id: int, amount: int, transaction_id: str, status: str = "pending") -> None:
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute(
            """
            INSERT INTO payments (user_id, amount, transaction_id, status, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (user_id, amount, transaction_id, status, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        await db.commit()


async def update_payment_status(transaction_id: str, status: str) -> None:
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute(
            "UPDATE payments SET status = ? WHERE transaction_id = ?",
            (status, transaction_id),
        )
        await db.commit()


async def get_payment(transaction_id: str):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM payments WHERE transaction_id = ?", (transaction_id,)
        ) as cursor:
            row = await cursor.fetchone()
            return dict(row) if row else None

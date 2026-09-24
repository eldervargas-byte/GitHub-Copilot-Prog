from datetime import datetime, timezone

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

post = {
    "author": "Maya Chen",
    "handle": "@mayachen",
    "avatar": "MC",
    "text": "A small idea can change the shape of a whole day. What are you making room for this week?",
    "likes": 128,
    "liked": False,
}

comments = [
    {
        "id": 1,
        "author": "Jordan Lee",
        "handle": "@jordanlee",
        "avatar": "JL",
        "text": "Making room for a slower morning and a little more curiosity.",
        "created_at": "Today, 9:14 AM",
    },
    {
        "id": 2,
        "author": "Priya Shah",
        "handle": "@priyashah",
        "avatar": "PS",
        "text": "This is the reminder I needed today.",
        "created_at": "Today, 8:52 AM",
    },
]
blocked_users = set()
blocked_comments = set()


def visible_comments():
    return [
        comment
        for comment in comments
        if comment["handle"] not in blocked_users
        and comment["id"] not in blocked_comments
    ]


@app.get("/")
def index():
    return render_template(
        "index.html",
        post=post,
        comments=visible_comments(),
        all_comments=comments,
        blocked_users=blocked_users,
        blocked_comments=blocked_comments,
    )


@app.post("/like")
def like():
    if not post["liked"]:
        post["likes"] += 1
        post["liked"] = True
    else:
        post["likes"] -= 1
        post["liked"] = False
    return redirect(url_for("index"))


@app.post("/comments")
def add_comment():
    text = request.form.get("comment", "").strip()
    if text:
        now = datetime.now(timezone.utc).astimezone()
        comments.insert(
            0,
            {
                "id": max((comment["id"] for comment in comments), default=0) + 1,
                "author": "You",
                "handle": "@you",
                "avatar": "YO",
                "text": text,
                "created_at": f"{now:%b} {now.day}, {now:%I:%M %p}",
            },
        )
    return redirect(url_for("index"))


@app.post("/block/user/<handle>")
def block_user(handle):
    handle = handle if handle.startswith("@") else f"@{handle}"
    if handle in blocked_users:
        blocked_users.remove(handle)
    else:
        blocked_users.add(handle)
    return redirect(url_for("index"))


@app.post("/block/comment/<int:comment_id>")
def block_comment(comment_id):
    if comment_id in blocked_comments:
        blocked_comments.remove(comment_id)
    else:
        blocked_comments.add(comment_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
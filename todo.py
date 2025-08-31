#!/usr/bin/env python3
import csv, argparse, os, sys

FILE = "todo.csv"

def load():
    items = []
    if not os.path.exists(FILE):
        return items
    with open(FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            items.append({
                "id": int(row["id"]),
                "title": row["title"],
                "done": row["done"] == "1",
            })
    return items

def save(items):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "title", "done"])
        w.writeheader()
        for it in items:
            w.writerow({
                "id": it["id"],
                "title": it["title"],
                "done": "1" if it["done"] else "0",
            })

def cmd_add(title):
    items = load()
    next_id = max([it["id"] for it in items], default=0) + 1
    items.append({"id": next_id, "title": title, "done": False})
    save(items)
    print(f"Added #{next_id}: {title}")

def cmd_list():
    items = load()
    if not items:
        print("(empty)")
        return
    for it in items:
        mark = "x" if it["done"] else " "
        print(f"[{mark}] {it['id']:>3} {it['title']}")

def cmd_done(task_id):
    items = load()
    for it in items:
        if it["id"] == task_id:
            it["done"] = True
            save(items)
            print(f"Done #{task_id}")
            return
    print(f"ID {task_id} not found", file=sys.stderr)
    sys.exit(1)

def main():
    p = argparse.ArgumentParser(description="Very small TODO")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("add", help="add a task")
    pa.add_argument("title")

    sub.add_parser("list", help="show tasks")

    pd = sub.add_parser("done", help="mark as done")
    pd.add_argument("id", type=int)

    args = p.parse_args()
    if args.cmd == "add":
        cmd_add(args.title)
    elif args.cmd == "list":
        cmd_list()
    elif args.cmd == "done":
        cmd_done(args.id)

if __name__ == "__main__":
    main()
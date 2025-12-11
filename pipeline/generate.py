import json, datetime, pathlib
from summarize import make_brief

def build_prompt(brief):
    return (
        f"Concept art illustrating {', '.join(brief.themes)}. "
        f"Central symbol: {brief.symbol}. Setting: {brief.setting}. "
        f"Palette: {', '.join(brief.palette)}. Mood: {brief.mood}."
    )

def publish_assets():
    brief = make_brief(["dummy text"])
    today = datetime.date.today().isoformat()
    meta = {
        "date": today,
        "caption": brief.caption,
        "alt": f"Scorpio daily visual: {', '.join(brief.themes)}",
        "prompt": build_prompt(brief)
    }
    pathlib.Path("public").mkdir(exist_ok=True)
    with open("public/today.json", "w") as f:
        json.dump(meta, f, indent=2)

if __name__ == "__main__":
    publish_assets()

from dataclasses import dataclass

@dataclass
class VisualBrief:
    themes: list[str]
    symbol: str
    setting: str
    palette: list[str]
    mood: str
    caption: str

def make_brief(texts: list[str]) -> VisualBrief:
    return VisualBrief(
        themes=["perseverance", "focus"],
        symbol="Scorpio glyph",
        setting="winter dawn",
        palette=["deep crimson", "midnight blue", "gold"],
        mood="resolute, calm",
        caption="Brishchik: hold the line, move with care."
    )

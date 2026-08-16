import re

class AntiClicheDetector:
    """
    Rileva parole e formule generiche o abusate tipiche dei generatori AI.
    """
    CLICHE_WORDS = {
        "sogni", "stelle", "gabbia", "volare", "luce", "oscurità", "volare via",
        "spiegar le ali", "rinascere", "catene", "demoni interni", "battito",
        "cuore di pietra", "strada buia", "anima persa", "destino"
    }

    def analyze(self, text: str) -> dict:
        lines = [l.strip().lower() for l in text.split("\n") if l.strip() and not l.startswith("[")]
        if not lines:
            return {"anticliche_score": 10.0, "detected_cliches": []}

        found_cliches = []
        for line in lines:
            for word in self.CLICHE_WORDS:
                pattern = r'\b' + re.escape(word) + r'\b'
                if re.search(pattern, line):
                    found_cliches.append(word)

        unique_cliches = list(set(found_cliches))
        penalty = len(unique_cliches) * 2.0
        score = max(0.0, 10.0 - penalty)

        return {
            "anticliche_score": round(score, 1),
            "detected_cliches": unique_cliches
        }

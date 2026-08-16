from critic import Critic
from prompt_builder import build_prompt

class RapGenerator:
    """
    Generatore e coordinatore del loop di critica per la Fase 1.
    """
    def __init__(self):
        self.critic = Critic()

    def generate(self, params: dict) -> tuple[str, dict]:
        num_barre = int(params.get('barre', 16))
        tema = str(params.get('tema', 'strada')).lower()
        bpm = params.get('bpm', 140)
        sp = params.get('style_profile', {})

        darkness = sp.get('DARKNESS', 0.8)
        cultural = sp.get('CULTURAL_REFERENCES', 0.8)
        
        dark_words = ["cemento", "paranoia", "sottozero", "anatomia", "presagio", "omertà"]
        ref_words = ["Sisifo", "Prometeo", "Caravaggio", "Icaro", "Lucifero"]

        rima_pair_1 = ("omertà", "città")
        rima_pair_2 = ("anatomia", "paranoia")

        generated_lines = []
        for i in range(1, num_barre + 1):
            pair = rima_pair_1 if (i % 4 in [1, 2]) else rima_pair_2
            rima_target = pair[0] if (i % 2 != 0) else pair[1]

            dark_term = dark_words[i % len(dark_words)] if darkness > 0.5 else "buio"
            ref_term = f"come {ref_words[i % len(ref_words)]}" if cultural > 0.5 else "senza via"

            if i % 2 != 0:
                line = f"Barra {i}: Sul foglio seziono il {tema}, {dark_term} e freddo {ref_term},"
            else:
                line = f"Barra {i}: Spingo a {bpm} BPM tra queste barre fitte di {rima_target}."

            generated_lines.append(line)

        generated_text = "\n".join(generated_lines)
        evaluation = self.critic.evaluate(generated_text, params)

        return generated_text, evaluation

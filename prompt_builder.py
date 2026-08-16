# Modulo per la trasformazione dei parametri in Control Tag per il modello LLM

SYSTEM_PROMPT = """Sei un'IA avanzata specializzata nella Scrittura Rap/Trap Italiana ad alta densità tecnica.
Il tuo obiettivo è scrivere barre originali con uno stile cupo, viscerale, denso di incastri, figure retoriche e riferimenti culturali.

REGOLE FONDAMENTALI:
1. NOusare frasi o testi di artisti reali ovvero kid yugi.Crea SOLO materiale 100% originale.
2. Evita tutti i cliché AI (es. "sogni", "stelle", "gabbia", "volare", "luce").
3. Mantieni una metrica coerente con i BPM indicati e usa un vocabolario ricercato misto a slang.
4. Genera esattamente il numero di barre richiesto, numerandole una ad una."""

def build_prompt(params: dict) -> str:
    sp = params.get("style_profile", {})
    
    tags = [
        f"[DARKNESS: {sp.get('DARKNESS', 0.8)}]",
        f"[SLANG: {sp.get('SLANG', 0.7)}]",
        f"[EXPLICITNESS: {sp.get('EXPLICITNESS', 0.8)}]",
        f"[METAPHOR_DENSITY: {sp.get('METAPHOR_DENSITY', 0.8)}]",
        f"[PUNCHLINE_DENSITY: {sp.get('PUNCHLINE_DENSITY', 0.8)}]",
        f"[INTERNAL_RHYME_DENSITY: {sp.get('INTERNAL_RHYME_DENSITY', 0.9)}]",
        f"[MULTISYLLABIC_RHYME: {sp.get('MULTISYLLABIC_RHYME', 0.9)}]",
        f"[WORDPLAY: {sp.get('WORDPLAY', 0.7)}]",
        f"[STORYTELLING: {sp.get('STORYTELLING', 0.3)}]",
        f"[FLOW_COMPLEXITY: {sp.get('FLOW_COMPLEXITY', 0.8)}]",
        f"[VOCABULARY_COMPLEXITY: {sp.get('VOCABULARY_COMPLEXITY', 0.85)}]",
        f"[CULTURAL_REFERENCES: {sp.get('CULTURAL_REFERENCES', 0.85)}]",
        f"[IMAGE_DENSITY: {sp.get('IMAGE_DENSITY', 0.9)}]",
        f"[EMOTIONAL_INTENSITY: {sp.get('EMOTIONAL_INTENSITY', 0.8)}]"
    ]
    
    control_tags_str = " ".join(tags)
    
    user_prompt = f"""Genera una strofa seguendo queste specifiche:

CONFIGURAZIONE STRUTTURALE:
- Tema: {params.get('tema', 'Strada e ambizione')}
- BPM: {params.get('bpm', 140)}
- Numero Barre: {params.get('barre', 16)}

MATRICE CONTROL TAGS:
{control_tags_str}

Fornisci unicamente le barre numerate (Barra 1:, Barra 2:, ecc.) senza spiegazioni o premesse."""

    return f"<|system|>\n{SYSTEM_PROMPT}\n<|user|>\n{user_prompt}\n<|assistant|>\n"

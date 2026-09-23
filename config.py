# =====================================================================
#  config.py  —  Settings for the LLB RAG project
# ---------------------------------------------------------------------------
#  Everything you might want to tweak lives here, in one readable place,
#  so you don't have to dig through the notebook cells.
#  Edit a value, then re-run the notebook from the top.
# =====================================================================

# --- Where the project lives inside Google Drive ---------------------
# This is the standard path after you mount Drive in Colab.
# Change only if you renamed the root folder.
PROJECT_ROOT = "/content/drive/MyDrive/LLB RAG"

DOCUMENTS_DIR = PROJECT_ROOT + "/documents"   # your source files (you add these)
VECTOR_DB_DIR = PROJECT_ROOT + "/vector_db"   # auto-created database (don't touch)


# --- Which semesters to load ----------------------------------------
# The notebook scans documents/ recursively. To include everything,
# leave this as ["all"]. To work on specific semesters only (faster),
# list them, e.g. ["sem2"] or ["sem1", "sem2"].
SEMESTERS_TO_LOAD = ["all"]


# --- Chunking settings ----------------------------------------------
# How documents are split into searchable pieces.
#  - Bigger CHUNK_SIZE  = more context per piece, but less precise retrieval
#  - Bigger CHUNK_OVERLAP = fewer sentences cut across boundaries
# Good starting point for study notes: 800 / 120.
CHUNK_SIZE = 800       # characters per chunk
CHUNK_OVERLAP = 120    # characters shared between neighbouring chunks


# --- Embedding model (Stage 2) --------------------------------------
# Free, offline, downloaded once. all-MiniLM-L6-v2 is small and fast.
# A stronger (slower) option: "all-mpnet-base-v2".
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


# --- Retrieval settings (Stage 3) -----------------------------------
# How many chunks to fetch per question.
#  - Too few  -> may miss relevant context
#  - Too many -> adds noise, slower generation
TOP_K = 4


# --- Generation model (Stage 4) -------------------------------------
# Local LLM served by Ollama. llama3.2:3b is light enough for modest
# hardware. On a stronger machine try "llama3.1:8b" for better answers.
LLM_MODEL = "llama3.2:3b"


# --- File types to ingest -------------------------------------------
SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".txt"]

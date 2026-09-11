def chunk_text(text: str, page_number: int):

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    project_titles = [
        "Urban Water Quality Prediction Using Ubiquitous Data",
        "QueryTube – AI-Powered Semantic Video Search & Summarization System",
        "Agri AI – Smart Agriculture Intelligence & Marketplace Platform",
        "Observability and Event Intelligence Pipeline"
    ]

    chunks = []
    chunk_id = 0

    current_project = None

    for line in lines:

        # Check whether this line starts a new project
        matched_title = None

        for title in project_titles:
            if line.startswith(title):
                matched_title = title
                break

        # New project found
        if matched_title:

            # Save the previous project
            if current_project:
                chunks.append({
                    "chunk_id": chunk_id,
                    "page": page_number,
                    "text": " ".join(current_project)
                })

                chunk_id += 1

            # Start the new project
            current_project = [line]

            continue

        # Stop collecting the Agri AI project when the CV moves
        # into the next major section.
        if current_project:

            if line.startswith("SKILLS"):
                chunks.append({
                    "chunk_id": chunk_id,
                    "page": page_number,
                    "text": " ".join(current_project)
                })

                chunk_id += 1
                current_project = None

                continue

            current_project.append(line)

    # Save the final project
    if current_project:
        chunks.append({
            "chunk_id": chunk_id,
            "page": page_number,
            "text": " ".join(current_project)
        })

    return chunks
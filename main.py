"""Write one pitch sentence for the ridiculous-startup bounty to /output/entry.txt.

Concept: professional mourners -- grieving families pay trained strangers to
weep, wail, and eulogize at funerals, because a well-mourned funeral honors
the dead and comforts the living.
"""

import os

SENTENCE = (
    "Grieving families hire our trained professional mourners to weep, wail, "
    "and eulogize strangers at funerals \u2014 because a packed, tear-soaked "
    "send-off honors the dead and spares the family shame."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()

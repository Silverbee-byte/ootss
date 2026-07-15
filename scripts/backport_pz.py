import re

s = open('ootss-next.pz').read()

s = re.sub(r'^(level_select|actionkey\s+.*|render_height|default_height\s+.*)$', r'(\1)', s, flags=re.MULTILINE)

s = re.sub(r'^section\s+([\w.]+)$', r'(level \1)', s, flags=re.MULTILINE)

# Add "[ action Player ] -> [ action Player CharacterSwap ]" after RULES block
s = re.sub(
    r'(^={3,}\s*RULES\s*={3,}\s*\n)',
    r'\1[ action Player ] -> [ action Player CharacterSwap ]\n\n',
    s,
    flags=re.MULTILINE
)


with open('ootss.pz','w') as f:
    f.write(s);



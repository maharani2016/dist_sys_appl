from pathlib import Path

p = Path(__file__).parent / 'requirements.txt'
print('path=', p)
text = p.read_text('utf-16')
if 'asyncpg>=0.28.0' not in text:
    if not text.endswith('\n'):
        text += '\n'
    text += 'asyncpg>=0.28.0\n'
    p.write_text(text, 'utf-16')
    print('appended asyncpg>=0.28.0')
else:
    print('asyncpg already present')
print('last lines:')
print(text.strip().splitlines()[-5:])

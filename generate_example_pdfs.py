import os
from fpdf import FPDF

# Example data (provided by user)
examples = [
    {
        'label': 1,
        'subject': 'Generic Cialis, branded quality@',
        'email_to': 'the00@speedy.uwaterloo.ca',
        'email_from': '"Tomas Jacobs" <RickyAmes@aol.com>',
        'message': 'Content-Type: text/html;\nContent-Transfer-Encoding: 7Bit Do you feel the pressure to perform and not rising to the occasion?? Try V ia gr a ..... your anxiety will be a thing of the past and you will be back to your old self.'
    },
    {
        'label': 0,
        'subject': 'Typo in /debian/README',
        'email_to': 'debian-mirrors@lists.debian.org',
        'email_from': 'Yan Morin <yan.morin@savoirfairelinux.com>',
        'message': "Hi, i've just updated from the gulus and I check on other mirrors.\nIt seems there is a little typo in /debian/README file\n\nExample:\nhttp://gulus.usherbrooke.ca/debian/README\nftp://ftp.fr.debian.org/debian/README\n\n\"Testing, or lenny.  Access this release through dists/testing.  The\ncurrent tested development snapshot is named etch.  Packages which\nhave been tested in unstable and passed automated tests propogate to\nthis release.\"\n\netch should be replace by lenny like in the README.html\n\n\n\n-- \nYan Morin\nConsultant en logiciel libre\nyan.morin@savoirfairelinux.com\n514-994-1556\n\n\n-- \nTo UNSUBSCRIBE, email to debian-mirrors-REQUEST@lists.debian.org\nwith a subject of \"unsubscribe\". Trouble? Contact listmaster@lists.debian.org"
    }
]

# Output directory
output_dir = 'example_pdfs'
os.makedirs(output_dir, exist_ok=True)

for ex in examples:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    label_str = 'SPAM' if ex['label'] == 1 else 'NON-SPAM'
    pdf.cell(0, 10, f'Example: {label_str}', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"Subject: {ex['subject']}", ln=True)
    pdf.cell(0, 10, f"To: {ex['email_to']}", ln=True)
    pdf.cell(0, 10, f"From: {ex['email_from']}", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 8, f"Message:\n{ex['message']}")
    filename = f"{label_str.lower()}_example.pdf"
    pdf.output(os.path.join(output_dir, filename))

print('Example PDFs generated in', output_dir)

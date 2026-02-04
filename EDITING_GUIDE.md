# Bill of Rights Website - Editing Guide

## Quick Start: How to Add Your Information

### 1. **Edit Your Basic Info** (EASIEST)
Open `app.py` and find this section at the top:

```python
bill_data = {
    'title': 'The Student-Centered Bill of Rights',
    'name': 'Faisal Adeela',  # ← CHANGE YOUR NAME HERE
    'class': 'US History 2',   # ← CHANGE YOUR CLASS HERE
    'rights': [],              # ← Add rights below
    'reflection': ''           # ← Add reflection below
}
```

### 2. **Add Your Rights** (Copy & Paste Template)
Replace the `'rights': []` with your rights. Here's the template:

```python
'rights': [
    {
        'number': 1,
        'title': 'Right to [Your Right Title]',
        'explanation': 'One or two sentences explaining the right.',
        'example': 'A concrete real-life example of this right in action.',
        'is_social_issue': False  # Set to True if it addresses current social issues
    },
    {
        'number': 2,
        'title': 'Right to [Another Right]',
        'explanation': 'Your explanation here.',
        'example': 'Your example here.',
        'is_social_issue': False
    },
    # Add more rights...
]
```

### 3. **Add Your Reflection** (200-300 words)
Replace the `'reflection': ''` with your reflection text:

```python
'reflection': """Your 200-300 word reflection explaining your top three rights, 
why they matter, and how to balance them with community/school/home rules."""
```

### 4. **Mark Social Issues**
Set `'is_social_issue': True` for any rights addressing:
- Online Privacy
- Mental Health
- Freedom of Expression
- Or other current social issues

These will be highlighted with a special badge on the website.

## Features

✨ **Automatic Animations:**
- Fade-in effects when page loads
- Slide animations for section titles
- Scale-in animations as you scroll
- Subtle pulse effects on right numbers

🎨 **Professional Design:**
- Historical parchment paper theme
- Serif fonts for formal appearance
- Decorative borders
- Grade 10 assignment-ready styling

📱 **Fully Responsive:**
- Works on desktop, tablet, and mobile
- Print-friendly PDF export built in

## Viewing Your Website

The Flask server should be running on: **http://127.0.0.1:5000**

Just open that URL in your browser to see your Bill of Rights!

## Tips

- **Print to PDF:** Click "Print / PDF" button or press Ctrl+P
- **Smooth Scrolling:** Navigation buttons smoothly scroll to sections
- **Easy Editing:** All content is in `app.py` - just update the Python dictionary
- **No HTML/CSS Knowledge Needed:** Just edit the text in `app.py`

---

**Made for Grade 10 World History Assignment**

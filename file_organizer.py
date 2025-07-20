#!/usr/bin/env python3
"""
File Organizer CLI - Fájlok rendszerezése különböző kritériumok szerint
"""

import os
import sys
import shutil
import argparse
from datetime import datetime
from pathlib import Path
from collections import defaultdict
import mimetypes

def get_file_info(file_path):
    """Fájl információk összegyűjtése"""
    stat = os.stat(file_path)
    return {
        'name': os.path.basename(file_path),
        'path': file_path,
        'size': stat.st_size,
        'modified': datetime.fromtimestamp(stat.st_mtime),
        'created': datetime.fromtimestamp(stat.st_ctime),
        'extension': os.path.splitext(file_path)[1].lower(),
        'mime_type': mimetypes.guess_type(file_path)[0] or 'unknown'
    }

def organize_by_extension(files, target_dir):
    """Rendszerezés kiterjesztés szerint"""
    print("📁 Rendszerezés kiterjesztés szerint...")
    
    for file_info in files:
        ext = file_info['extension']
        if not ext:
            ext = 'no_extension'
        else:
            ext = ext.lstrip('.')
        
        # Cél könyvtár létrehozása
        dest_dir = os.path.join(target_dir, f"{ext}_files")
        os.makedirs(dest_dir, exist_ok=True)
        
        # Fájl mozgatása
        dest_path = os.path.join(dest_dir, file_info['name'])
        try:
            shutil.move(file_info['path'], dest_path)
            print(f"  ✓ {file_info['name']} → {ext}_files/")
        except Exception as e:
            print(f"  ✗ Hiba {file_info['name']} mozgatásakor: {e}")

def organize_by_type(files, target_dir):
    """Rendszerezés fájltípus szerint"""
    print("📂 Rendszerezés fájltípus szerint...")
    
    # Fájltípus kategóriák
    categories = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico'],
        'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
        'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
        'archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
        'code': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.cs', '.php', '.rb', '.go', '.rs'],
        'executables': ['.exe', '.msi', '.deb', '.rpm', '.dmg', '.app'],
        'data': ['.json', '.xml', '.csv', '.sql', '.db', '.sqlite']
    }
    
    for file_info in files:
        ext = file_info['extension']
        category = 'others'
        
        # Kategória meghatározása
        for cat, extensions in categories.items():
            if ext in extensions:
                category = cat
                break
        
        # Cél könyvtár létrehozása
        dest_dir = os.path.join(target_dir, category)
        os.makedirs(dest_dir, exist_ok=True)
        
        # Fájl mozgatása
        dest_path = os.path.join(dest_dir, file_info['name'])
        try:
            shutil.move(file_info['path'], dest_path)
            print(f"  ✓ {file_info['name']} → {category}/")
        except Exception as e:
            print(f"  ✗ Hiba {file_info['name']} mozgatásakor: {e}")

def organize_by_date(files, target_dir, date_format):
    """Rendszerezés dátum szerint"""
    print(f"📅 Rendszerezés dátum szerint ({date_format})...")
    
    for file_info in files:
        date_obj = file_info['modified']
        
        if date_format == 'year':
            folder_name = str(date_obj.year)
        elif date_format == 'month':
            folder_name = f"{date_obj.year}-{date_obj.month:02d}"
        elif date_format == 'day':
            folder_name = f"{date_obj.year}-{date_obj.month:02d}-{date_obj.day:02d}"
        else:
            folder_name = str(date_obj.year)
        
        # Cél könyvtár létrehozása
        dest_dir = os.path.join(target_dir, folder_name)
        os.makedirs(dest_dir, exist_ok=True)
        
        # Fájl mozgatása
        dest_path = os.path.join(dest_dir, file_info['name'])
        try:
            shutil.move(file_info['path'], dest_path)
            print(f"  ✓ {file_info['name']} → {folder_name}/")
        except Exception as e:
            print(f"  ✗ Hiba {file_info['name']} mozgatásakor: {e}")

def organize_by_size(files, target_dir):
    """Rendszerezés méret szerint"""
    print("📊 Rendszerezés méret szerint...")
    
    for file_info in files:
        size = file_info['size']
        
        if size < 1024:  # < 1KB
            folder_name = 'small_files'
        elif size < 1024 * 1024:  # < 1MB
            folder_name = 'medium_files'
        elif size < 1024 * 1024 * 100:  # < 100MB
            folder_name = 'large_files'
        else:  # >= 100MB
            folder_name = 'huge_files'
        
        # Cél könyvtár létrehozása
        dest_dir = os.path.join(target_dir, folder_name)
        os.makedirs(dest_dir, exist_ok=True)
        
        # Fájl mozgatása
        dest_path = os.path.join(dest_dir, file_info['name'])
        try:
            shutil.move(file_info['path'], dest_path)
            print(f"  ✓ {file_info['name']} → {folder_name}/")
        except Exception as e:
            print(f"  ✗ Hiba {file_info['name']} mozgatásakor: {e}")

def preview_organization(files, method, **kwargs):
    """Rendszerezés előnézete"""
    print(f"\n🔍 Előnézet - {method} szerint:")
    print("-" * 50)
    
    groups = defaultdict(list)
    
    for file_info in files:
        if method == 'extension':
            key = file_info['extension'].lstrip('.') if file_info['extension'] else 'no_extension'
        elif method == 'type':
            categories = {
                'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico'],
                'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
                'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
                'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
                'archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
                'code': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.cs', '.php', '.rb', '.go', '.rs'],
                'executables': ['.exe', '.msi', '.deb', '.rpm', '.dmg', '.app'],
                'data': ['.json', '.xml', '.csv', '.sql', '.db', '.sqlite']
            }
            key = 'others'
            for cat, extensions in categories.items():
                if file_info['extension'] in extensions:
                    key = cat
                    break
        elif method == 'date':
            date_obj = file_info['modified']
            date_format = kwargs.get('date_format', 'year')
            if date_format == 'year':
                key = str(date_obj.year)
            elif date_format == 'month':
                key = f"{date_obj.year}-{date_obj.month:02d}"
            elif date_format == 'day':
                key = f"{date_obj.year}-{date_obj.month:02d}-{date_obj.day:02d}"
        elif method == 'size':
            size = file_info['size']
            if size < 1024:
                key = 'small_files'
            elif size < 1024 * 1024:
                key = 'medium_files'
            elif size < 1024 * 1024 * 100:
                key = 'large_files'
            else:
                key = 'huge_files'
        
        groups[key].append(file_info['name'])
    
    for group, files_list in sorted(groups.items()):
        print(f"\n📁 {group}/ ({len(files_list)} fájl)")
        for file_name in sorted(files_list)[:5]:  # Csak az első 5 fájl
            print(f"  • {file_name}")
        if len(files_list) > 5:
            print(f"  ... és még {len(files_list) - 5} fájl")

def main():
    parser = argparse.ArgumentParser(
        description="Fájlok rendszerezése különböző kritériumok szerint",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Példák:
  python file_organizer.py --method extension              # Kiterjesztés szerint
  python file_organizer.py --method type                   # Fájltípus szerint
  python file_organizer.py --method date --date-format month  # Hónap szerint
  python file_organizer.py --method size                   # Méret szerint
  python file_organizer.py --preview --method extension    # Előnézet
        """
    )
    
    parser.add_argument(
        '--method', 
        choices=['extension', 'type', 'date', 'size'],
        required=True,
        help='Rendszerezés módja'
    )
    
    parser.add_argument(
        '--date-format',
        choices=['year', 'month', 'day'],
        default='year',
        help='Dátum formátum (csak --method date esetén)'
    )
    
    parser.add_argument(
        '--preview',
        action='store_true',
        help='Csak előnézet, nem mozgatja a fájlokat'
    )
    
    parser.add_argument(
        '--target-dir',
        default='organized_files',
        help='Cél könyvtár neve (alapértelmezett: organized_files)'
    )
    
    parser.add_argument(
        '--include-hidden',
        action='store_true',
        help='Rejtett fájlok is'
    )

    parser.add_argument(
        '--source-dir',
        default='.',
        help='Forrás könyvtár (alapértelmezett: aktuális mappa)'
    )
    
    args = parser.parse_args()

    # Forrás könyvtár
    source_dir = os.path.abspath(args.source_dir)
    print(f"📂 Munkamappa: {source_dir}")

    # Fájlok listázása
    files = []
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)

        # Könyvtárakat kihagyjuk
        if os.path.isdir(item_path):
            continue

        # Rejtett fájlok kezelése
        if item.startswith('.') and not args.include_hidden:
            continue

        # Script saját magát kihagyjuk
        if item_path == os.path.abspath(__file__):
            continue

        files.append(get_file_info(item_path))

    if not files:
        print("❌ Nincsenek rendszerezhető fájlok a mappában!")
        return

    print(f"📋 Talált fájlok: {len(files)}")

    # Előnézet vagy végrehajtás
    if args.preview:
        preview_organization(files, args.method, date_format=args.date_format)
        return

    # Megerősítés kérése
    response = input(f"\nBiztosan rendszerezed a {len(files)} fájlt? (i/n): ")
    if response.lower() not in ['i', 'igen', 'y', 'yes']:
        print("❌ Megszakítva.")
        return

    # Cél könyvtár létrehozása
    target_path = os.path.join(source_dir, args.target_dir)
    os.makedirs(target_path, exist_ok=True)

    # Rendszerezés végrehajtása
    if args.method == 'extension':
        organize_by_extension(files, target_path)
    elif args.method == 'type':
        organize_by_type(files, target_path)
    elif args.method == 'date':
        organize_by_date(files, target_path, args.date_format)
    elif args.method == 'size':
        organize_by_size(files, target_path)

    print(f"\n✅ Rendszerezés kész! Fájlok: {args.target_dir}/")

if __name__ == "__main__":
    main()

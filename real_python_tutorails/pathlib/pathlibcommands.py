from pathlib import Path

if __name__ == "__main__":
    base_dir = Path("src")
    print(base_dir)

    child_dir = base_dir /"stuff"
    print(child_dir)

    file_path = child_dir / "__init__/py"
    print(file_path)

    print(file_path.parts)

    print(file_path.parents)

    for parent in file_path.parents:
        print(parent)

    print(file_path.parent)

    file_path = Path("src/module.py")
    print(file_path.name)

    file_path = Path("srsc/stuff/somefile.tar.gz")
    print(file_path.suffixes)
    print(file_path.suffix)

    print(file_path.stem)

    print(file_path.is_absolute())

    file_path = Path("src").joinpath("stuff").joinpath("__init__.py")
    print(file_path)

    print(file_path.cwd())

    print(Path.home())

    print(file_path.exists())

    print(file_path.expanduser())

    print(file_path.is_dir())

    print(file_path.is_file())

    print(file_path.is_absolute())

    base_path = Path("/home/msr/books/python/progs/real_python_tutorails/")
    contents = [ content for content in base_path.iterdir()]
    print(contents)

    #dir_path = Path("/home/msr/books/python/progs/real_python_tutorails/pathlib/temp_dir")
    #dir_path.mkdir(parents = True)

    

    dir_path = Path("/home/msr/books/python/progs/real_python_tutorails/pathlib/")
    file_path = dir_path.glob("*.py")
    print(list(file_path))

    file_path = dir_path.rglob("*.py")
    print(list(file_path))
    
    
    
    print(dir_path.joinpath("main.py").is_file())
    
    with Path(dir_path.joinpath("main.py")) as f:
        contents = open(f, "r")
        for line in contents:
            print(line)
        
    
        
    
                    
    
        

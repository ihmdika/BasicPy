import runner

def main():
    print("Welcome to BasicPy interpreter! Type 'exit' to exit.")
    
    while True:
        text = input("basic > ")
        
        if text.strip().lower() == 'exit':
            print("Exiting BasicPy. Goodbye!")
            break
        
        result, error = runner.run("<stdin>", text)
        
        if error:
            print(f"Error: {error}")
        else:
            print(result)

if __name__ == "__main__":
    main()

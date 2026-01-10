import openai

# Replace this with your new OpenAI API key
openai.api_key = "sk-svcacct-0xAlGsirrUg164qxH1ArT3BlbkFJ5x7hOrytwVFxWi2SciNb"

def chat_with_gpt():
    print("🤖 ChatBot (type 'exit' to quit)\n")

    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit']:
            print("ChatBot: Goodbye! 👋")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # You can change this to "gpt-4" if you have access
                messages=messages
            )

            reply = response['choices'][0]['message']['content']
            messages.append({"role": "assistant", "content": reply})
            print("ChatBot:", reply)

        except Exception as e:
            print("Error:", e)
            break

if __name__ == "__main__":
    chat_with_gpt()







#include <bits/stdc++.h>
using namespace std;
int main() {
    // int a=5,b=10;
    // char*ch=new char;
    // *ch='a';
    // cout<< ch<<endl;
    // auto sayHello = [&]() { // capture a and b by reference
    // int dc = a + b;
    // cout << "Sum is " << dc << endl;
    // };
    // sayHello();
    int n;
    cin >> n ;
    int *arr = new int[n];
    cout << arr[3];
    return 0;
}
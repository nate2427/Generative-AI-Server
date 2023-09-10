

def query_agent(query_string):
    from . import data_service_agent

    response = data_service_agent.chat(query_string)
    return response.response


if __name__ == "__main__":
    query = "what good restaurants are in toronto"
    print(f"Question: {query}\n")
    answer = query_agent(query)
    print(f"Answer: {answer}\n")

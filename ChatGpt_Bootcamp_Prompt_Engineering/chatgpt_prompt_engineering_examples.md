# ChatGPT Prompt Engineering Examples

## Summarization Prompt

**Prompt:**
```
Summarize the following paragraph:

Artificial intelligence is a branch of computer science focused on building smart machines capable of performing tasks that typically require human intelligence. AI is an interdisciplinary science with multiple approaches, but advancements in machine learning and deep learning are creating a paradigm shift in virtually every sector of the tech industry.
```

**ChatGPT Response:**
```
Artificial intelligence is a computer science field focused on creating smart machines that mimic human intelligence, with machine learning and deep learning driving major tech advancements.
```

## Translation Prompt

**Prompt:**
```
Translate the following English sentence into French:

'The weather is nice today and we are going to the park.'
```

**ChatGPT Response:**
```
Le temps est agréable aujourd'hui et nous allons au parc.
```

## Code Generation Prompt

**Prompt:**
```
Write a Python function that checks if a number is prime.
```

**ChatGPT Response:**
```
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

## Chain-of-Thought Reasoning Prompt

**Prompt:**
```
If a train travels at 60 miles per hour for 2.5 hours, how far does it go? Let's think step by step.
```

**ChatGPT Response:**
```
Step 1: The speed is 60 miles per hour.
Step 2: The time is 2.5 hours.
Step 3: Distance = Speed × Time = 60 × 2.5 = 150 miles.

Answer: 150 miles.
```

## Persona-Based Prompt

**Prompt:**
```
You are a friendly tour guide in Rome. Recommend a one-day itinerary for a first-time visitor.
```

**ChatGPT Response:**
```
Welcome to Rome! Start your day at the Colosseum, then walk through the Roman Forum. Grab lunch near the Pantheon, visit the Trevi Fountain, and end your day with sunset views from the Spanish Steps. Buon viaggio!
```


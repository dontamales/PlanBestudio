CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question_text TEXT NOT NULL,
    answer_text TEXT NOT NULL
);
INSERT INTO questions (question_text, answer_text) VALUES
('What is the capital of France?', 'Paris'),
('What is 2 + 2?', '4');
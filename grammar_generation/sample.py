import ideaToText

GRAMMAR_PATH = 'grammars/cereal'

def main():
	sampler = ideaToText.Sampler(GRAMMAR_PATH)

	for i in range(10):
		sample = sampler.singleSample()
		text = sample['text']
		rubric = sample['rubric']
		print(text)
		print(rubric)
		print('----')


if __name__ == '__main__':
	main()

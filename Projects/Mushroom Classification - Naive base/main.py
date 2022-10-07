import csv
import random
# Names : Mona , Nimrod , Mohammad Joubat , Jehad , Mhinkkye ,Magdi, Rani
attributes_yes_list = []
attributes_no_list = []
positive_dataset = []
negative_dataset = []
pos_train = []
neg_train = []
training_data = []
test_data = []
g_attributes = []  # doesn't include poisonous or edible columns
g_attributes_dictionary = {}
class data_class:
    def prepare_datasets(self):
        self.training_data = training_data
        self.test_data = test_data
        # DATASET = "agricus-lepiota.csv"
        # ATTRIBUTES = 'agaricus-lepiota.names.csv'
        with open('/Users/mhinkyu/MyLab/Code Lab/OOP Database/Mushroom.csv', 'r+') as dataset_file:
            dataset_lines = dataset_file.readlines()
        for line in dataset_lines:
            attributes = line.split(',')
            # Get rid of newline character on last attribute
            attributes[-1] = attributes[-1].strip()
            if attributes[0] == 'e':
                # Two options "e" or P :
                positive_dataset.append((attributes[0], attributes[1:]))
            else:
                negative_dataset.append((attributes[0], attributes[1:]))
        while len(positive_dataset) and len(negative_dataset):
            # running at all data randomly
            rand_pos = random.randint(0, min(len(positive_dataset), len(negative_dataset)) - 1)
            self.training_data.append(positive_dataset.pop(rand_pos))
            self.training_data.append(negative_dataset.pop(rand_pos))
            # Training data ---> bulding the model
            if len(positive_dataset) and len(negative_dataset):
                rand_pos = random.randint(0, min(len(positive_dataset), len(negative_dataset)) - 1)
                self.training_data.append(positive_dataset.pop(rand_pos))
                self.training_data.append(negative_dataset.pop(rand_pos))
        #while len(positive_dataset) and len(negative_dataset):
            # Testing data --> testing the model
            if len(positive_dataset) and len(negative_dataset):
                rand_pos = random.randint(0, min(len(positive_dataset), len(negative_dataset)) - 1)
                self.test_data.append(positive_dataset.pop(rand_pos))
                self.test_data.append(negative_dataset.pop(rand_pos))
class attribute_class:
    def parse_attributes(self):
        # ATTRIBUTES = agaricus-lepiota.names.csv'
        with open("/Users/mhinkyu/MyLab/Code Lab/OOP Database/agaricus-lepiota.names.csv", 'r+') as attributes_file:
            # print(attributes_file)
            attributes_lines = attributes_file.readlines()
            # print(attributes_lines)
        for line in attributes_lines:
            #print(attributes_lines)
            pair = line.strip().split()
            g_attributes.append(pair[0])
            g_attributes_dictionary[pair[0]] = pair[1].split(',')
    def prepare_attribute_lists(self):
        attr_count = 0
        for i in range(len(g_attributes)):
            attributes_yes_list.append([])
            attributes_no_list.append([])
        for i in attributes_yes_list:
            for j in range(12):
                i.append(0)
        for i in attributes_no_list:
            for j in range(12):
                i.append(0)
        for attr in g_attributes:
            val_count = 0
            for value in g_attributes_dictionary[attr]:
                for example in training_data:
                    if value == example[1][attr_count] and example[0] == 'e':
                        attributes_yes_list[attr_count][val_count] += 1
                val_count += 1
            attr_count += 1
        attr_count = 0
        for attr in g_attributes:
            val_count = 0
            for value in g_attributes_dictionary[attr]:
                for example in training_data:
                    if value == example[1][attr_count] and example[0] == 'p':
                        attributes_no_list[attr_count][val_count] += 1
                val_count += 1
            attr_count += 1
class naive_class:
    def naive_bayes(self, example, neg, pos):
        count = 0
        pos_prob = 1.0
        neg_prob = 1.0
        for attr in example:
            pos_prob *= attributes_yes_list[count][g_attributes_dictionary[g_attributes[count]].index(attr)]
            neg_prob *= attributes_no_list[count][g_attributes_dictionary[g_attributes[count]].index(attr)]
            count += 1
        if neg_prob > pos_prob:
            return 'p'
        else:
            return 'e'
if __name__ == '__main__':
    preperation = data_class().prepare_datasets()
    # prepare_datasets()
    attributes = attribute_class.parse_attributes(test_data)
    # parse_attributes()
    attribute_lists = attribute_class.prepare_attribute_lists(attributes_no_list)
    # prepare_attribute_lists()
    print("done with tables")
    num_pos = 0
    num_neg = 0
    for i in training_data:
        if i[0] == 'e':
            num_pos += 1
            pos_train.append(i[1])
        else:
            num_neg += 1
            neg_train.append(i[1])
    correct = 0
    mistake_counter = 0
    for ex in test_data:
        actual = ex[0]
        naive = naive_class().naive_bayes(ex[1], 0, 0)
        calculated = naive
        # calculated = naive(ex[1], num_neg, num_pos)
        print("actual: %s classified: %s " % (actual, calculated))
        if actual == calculated:
            correct += 1
        else:
            mistake_counter += 1
    print(f'There are a total of {mistake_counter} wrong predictions,and total of {correct} correct predictions, out of {len(test_data)} predictions, tested.')
    print("Accuracy percentage is: %f " % (float(correct * 100) / float(len(test_data))))

print("Lines of training data:",len(training_data))
print("Lines of testing data:",len(test_data))
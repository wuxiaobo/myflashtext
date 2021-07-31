import os
import string
import io

class MyFlashtext(object):
    '''
    存在问题是对中文match出现匹配异常的bug，重写extract_keywords 方法后已修正。
    '''
    def __init__(self, case_sensitive=False):
        self._keyword = '_keyword_'
        self._white_space_chars = set(['.', '\t', '\n', '\a', ' ', ','])
        self.keyword_trie_dict = dict()
        self.case_sensitive = case_sensitive
        self._terms_in_trie = 0
        self.non_word_boundaries = set(string.digits + string.ascii_letters + '_')

    def __getitem__(self):
        return self.keyword_trie_dict

    def __setitem__(self, keyword, clean_name=None):
        status = False
        if not clean_name and keyword:
            clean_name = keyword

        if keyword and clean_name:
            if not self.case_sensitive:
                keyword = keyword.lower()
            current_dict = self.keyword_trie_dict
            for letter in keyword:
                current_dict = current_dict.setdefault(letter, {})
            if self._keyword not in current_dict:
                status = True
                self._terms_in_trie += 1
            current_dict[self._keyword] = clean_name
        return status

    def add_keyword(self, keyword, clean_name=None):
        return self.__setitem__(keyword, clean_name)

    def get_dict(self):
        return self.__getitem__()

    def add_keywords_from_list(self, keyword_list):
        # if not isinstance(keyword_list, list):
        #     raise AttributeError("keyword_list should be a list")

        for keyword in keyword_list:
            self.add_keyword(keyword)

    def extract_keywords(self, sentence, span_info=False):
        keywords_extracted = []
        if not sentence:
            # if sentence is empty or none just return empty list
            return keywords_extracted
        if not self.case_sensitive:
            sentence = sentence.lower()
        current_dict = self.keyword_trie_dict
        sequence_start_pos = 0
        sequence_end_pos = 0
        idx = 0
        sentence_len = len(sentence)
        while idx < sentence_len:
            char = sentence[idx]
            if self._keyword in current_dict or char in current_dict:
                # update longest sequence found
                sequence_found = None
                longest_sequence_found = None
                is_longer_seq_found = False
                if self._keyword in current_dict:
                    sequence_found = current_dict[self._keyword]
                    longest_sequence_found = current_dict[self._keyword]
                    sequence_end_pos = idx
                # re look for longest_sequence from this position
                if char in current_dict:
                    current_dict_continued = current_dict[char]
                    idy = idx + 1
                    while idy < sentence_len:
                        inner_char = sentence[idy]
                        if self._keyword in current_dict_continued:
                            longest_sequence_found = current_dict_continued[self._keyword]
                            sequence_end_pos = idy
                            is_longer_seq_found = True
                        if inner_char in current_dict_continued:
                            current_dict_continued = current_dict_continued[inner_char]
                        else:
                            break
                        idy += 1
                    else:
                        # end of sentence reached.
                        if self._keyword in current_dict_continued:
                            # update longest sequence found
                            longest_sequence_found = current_dict_continued[self._keyword]
                            sequence_end_pos = idy
                            is_longer_seq_found = True
                    if is_longer_seq_found:
                        idx = sequence_end_pos
                    else:
                        idx += 1
                current_dict = self.keyword_trie_dict
                if longest_sequence_found:
                    keywords_extracted.append((longest_sequence_found, sequence_start_pos, idx))
            else:
                current_dict = self.keyword_trie_dict
                idx += 1
            if idx + 1 >= sentence_len:
                if self._keyword in current_dict:
                    sequence_found = current_dict[self._keyword]
                    keywords_extracted.append((sequence_found, sequence_start_pos, sentence_len))
            sequence_start_pos = idx
        if span_info:
            return keywords_extracted
        return [{"word":value[0],"index":[value[1], value[2]]}  for value in keywords_extracted]
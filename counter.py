class Counter(object):

    # fields
    values = dict()
    @classmethod
    def get_values(cls):
        return cls.values
        
    access = dict()
    @classmethod
    def get_access(cls):
        return cls.access
        
    accom = dict()
    @classmethod
    def get_accom(cls):
        return cls.accom

    @classmethod
    def get_new_token(cls, flow_name):
        # token = str(hash(flow_name))
        token = flow_name
        cls.values[token] = []
        cls.access[token] = True
        cls.accom[token] = []
        return token
        pass

    @classmethod
    def get_count(cls, token):
        return cls.values[token]
        pass
    @classmethod
    def deinc(cls, token):
        cls.values[token] -= 1
        pass
    @classmethod
    def clear(cls, token):
        cls.values[token] = []
        pass
    @classmethod
    def inc(cls, token, value):
        if (cls.access[token]):
            cls.values[token].append(value)
            print('Append to ({0}) values'.format(token))
            pass
        else:
            cls.accom[token].append(value)
            print('Accom to ({0}) values'.format(token))
            pass
        print(cls.values)
        pass

    @classmethod
    def resume_counting(cls, token):
        if (cls.access[token]):
            print('ERROR: Error with counters access')
            pass
        else:
            for i in cls.accom[token]:
                cls.values[token].append(i)
                continue
            cls.access[token] = True
            pass
        pass
    @classmethod
    def pause_counting(cls, token):
        cls.access[token] = False
        pass
    @classmethod
    def reset(cls):
        cls.values = dict()
        pass


if __name__ == '__main__':
    
    if (False):
        token1 = Counter.get_new_token('First stream')
        Counter.inc(token1)
        
        token2 = Counter.get_new_token('Second stream')
        Counter.inc(token2)
        Counter.inc(token2)

        Counter.reset()
        pass

    pass
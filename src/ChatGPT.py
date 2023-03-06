#!python3

import openai
import json
import GT2S
import datetime

class ChatGPT:
    key_path="private/api_keys"
    base_hist_path="record/chat_hist_"
    hist_path=None
    model="gpt-3.5-turbo"
    usage={"prompt_tokens": 0, "completion_tokens": 0}
    gt2s=None
    commands= dict()

    system_msg = None
    msg_hist = list()

    def __init__(self, system_msg, preload_hist=None, speech=False):
        with open(self.key_path, "r") as priv:
            api_key = priv.readline().rstrip('\n')
            openai.api_key = api_key

        self.set_system_msg(system_msg)
        self.set_msg_hist(preload_hist)
        self.gen_hist_path()
        self.speech = speech
        if speech:
            self.gt2s = GT2S.GT2S()

    def set_commands(self, commands={}):
        self.commands.update(commands)

    def set_system_msg(self, system_msg):
        self.system_msg = system_msg

    def set_msg_hist(self, preload_hist=None):
        self.msg_hist.clear()
        if preload_hist:
            self.msg_hist.update(preload_hist)
        else:
            self.msg_hist.append({"content": self.system_msg, "role": "system"})

    def gen_hist_path(self):
        self.hist_path = self.base_hist_path + str(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))

    def print_content(self, data):
        msg = json.dumps(data["content"], indent=2, ensure_ascii=False)
        print(" [o] {0: <12} said: {1}".format(data["role"], msg))

    def reset(self):
        print(" [o] reset!")
        self.finalize()
        self.set_msg_hist()
        self.gen_hist_path()

    def user_ask(self, msg):
        data = {"content": msg + " Current Time: "+datetime.datetime.now().strftime("%H:%M:%S"), "role": "user"}
        self.msg_hist.append(data)
        response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.msg_hist
                )
        self.print_content(data)

        for choice in response["choices"]:
            resp_raw_data = choice["message"]
            if choice["finish_reason"] == "stop" or choice["finish_reason"] is None:
                data = openai.util.convert_to_dict(resp_raw_data)
                self.print_content(data)

                # run the provided handler if key exists
                if (data["content"] in self.commands.keys()):
                    self.commands[data["content"]]()
                else:
                    self.msg_hist.append(data)

                if self.gt2s is not None:
                    self.gt2s.text2speech(data["content"], 1.2)
            else:
                data = openai.util.convert_to_dict(resp_raw_data)
                print(" [{0}] Debug:\n{1}".format(choice["finish_reason"], data))

        self.usage["prompt_tokens"] += response["usage"]["prompt_tokens"]
        self.usage["completion_tokens"] += response["usage"]["completion_tokens"]

    def finalize(self):
        with open(self.hist_path, "w") as hist:
            hist.write(str(self.msg_hist));

    def __del__(self):
        print("Usage:")
        print("  Prompt Tokens:       ", self.usage["prompt_tokens"])
        print("  Completion Tokens:   ", self.usage["completion_tokens"])
        print("")


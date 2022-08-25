# stable-diffusion-test

- <https://github.com/CompVis/stable-diffusion>
- <https://huggingface.co/CompVis>

Install `git` and `git-lfs`.

```shell
sudo apt install git git-lfs
```

Install `huggingface-cli` command.

- <https://pypi.org/project/huggingface-hub/>
- <https://huggingface.co/welcome>

```shell
pip3 install --upgrade huggingface-hub
```

Create a HuggingFace account.

- <https://huggingface.co/join>

(maybe skippable: Get access to the stable-diffusion weights.)

- <https://huggingface.co/CompVis>

Create a token for your HuggingFace account.

- <https://huggingface.co/settings/tokens>

Login CLI with the token.

```shell
huggingface-cli login
```

Install dependencies.

```shell
pip3 install -r requirements.txt
```

Start the FastAPI server.

```shell
uvicorn main:app
```

Send a request to the FastAPI server.

```shell
curl -X 'POST' 'http://127.0.0.1:8000/generate' -H 'Content-Type: application/json' -d '{"prompt":"a photograph of an astronaut riding a horse"}'
```

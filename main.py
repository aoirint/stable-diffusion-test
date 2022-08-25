# make sure you're logged in with `huggingface-cli login`
from datetime import datetime
from pathlib import Path
from torch import autocast
from diffusers import StableDiffusionPipeline
from fastapi import FastAPI
from pydantic import BaseModel
from pytorch_lightning import seed_everything

device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(
  "CompVis/stable-diffusion-v1-4",
  use_auth_token=True,
).to(device)

app = FastAPI()

class GenerateRequestModel(BaseModel):
  prompt: str

# curl -X 'POST' 'http://127.0.0.1:8000/generate' -H 'Content-Type: application/json' -d '{"prompt":"a photograph of an astronaut riding a horse"}'
@app.post('/generate')
def generate(params: GenerateRequestModel):
  prompt = params.prompt

  prompt = prompt.strip()

  now = datetime.now()
  output_dir = Path('outputs')
  output_dir.mkdir(parents=True, exist_ok=True)

  seed = 42
  seed_everything(seed)

  with autocast(device):
    image = pipe(prompt)["sample"][0]

  datestr = now.strftime('%Y-%m-%d_%H-%M-%S')
  stem = f'{datestr}'

  image.save(output_dir / f'{stem}.png')
  (output_dir /  f'{stem}.txt').write_text(prompt, encoding='utf-8')

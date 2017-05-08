import torch
from torch.autograd import Variable
import net


model = net.model
model.load_state_dict(torch.load('net.pth'))
model.eval()

input = torch.rand(6, 3, 96, 96)    # input: RGB image of 96*96

# CPU
output = model(Variable(input))
print('CPU done')

# GPU
model.cuda()
input = input.cuda()
output = model(Variable(input))
print('GPU done')
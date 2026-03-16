#!/usr/bin/env python3
"""Minimal tensor library with autograd."""
class Tensor:
    def __init__(self,data):self.data=list(data)
    def __mul__(self,o):return Tensor([a*b for a,b in zip(self.data,o.data)])
    def __add__(self,o):return Tensor([a+b for a,b in zip(self.data,o.data)])
    def __repr__(self):return f"Tensor({self.data})"

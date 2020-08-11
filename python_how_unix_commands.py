#!/usr/bin/env python3.6

#Simple example of how to use Unix commands from within a python script.
#Exemplos simples de como executar comandos Unix a partir de script em python.
import subprocess

subprocess.call(["uname", "-r"])
#This code gives the output of the command "uname -r", it should print the version of the kernel.
#Este codigo executa o comando "uname -r", este apresenta a versao do kernel em uso.

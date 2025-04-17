# 🏦 Sistema Bancário em Python

Este projeto foi desenvolvido como parte de um exercício do **Bootcamp da Digital Innovation One (DIO)**. O objetivo era colocar em prática os conceitos iniciais de programação em **Python**, criando um sistema bancário simples com operações básicas como **depósito**, **saque** e **emissão de extrato**.

## 🎯 Objetivo

Criar um sistema que simule funcionalidades de um banco digital, permitindo que o usuário interaja por meio do terminal para realizar as seguintes operações:

- Depósitos
- Saques (com regras definidas)
- Consulta de extrato
- Encerramento do programa

## ⚙️ Como funciona

O sistema funciona em um loop contínuo (`while True`) até que o usuário escolha a opção de **encerrar o programa** digitando `sair`.

As operações disponíveis são:

### ➕ `depositar`

- Solicita ao usuário o valor a ser depositado.
- Apenas valores positivos são aceitos.
- O valor é somado ao saldo e registrado no histórico.

### ➖ `sacar`

Antes de efetuar o saque, o sistema verifica:

- Se o limite diário de **3 saques** foi atingido.
- Se o valor informado é maior que **R$ 500,00**, que é o limite por saque.
- Se há **saldo suficiente** para realizar o saque.

Se todas as condições forem atendidas, o saque é realizado, descontado do saldo e registrado no histórico.

### 📄 `extrato`

- Exibe todas as operações realizadas (depósitos e saques).
- Mostra o **saldo atual**.

### ❌ `sair`

- Encerra o programa com uma mensagem de finalização.

## 💡 Exemplo de uso

```bash
Digite a operacao desejada: depositar
Digite a valor a ser depositado: 300

Digite a operacao desejada: sacar
Qual valor deseja sacar? 100

Digite a operacao desejada: extrato

------------- EXTRATO -----------------
    Depósito: + R$ 300.00
    Saque: - R$ 100.00
    Saldo atual: R$ 1200.00

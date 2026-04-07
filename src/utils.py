"""
Funções utilitárias para o projeto de Forecasting de Demanda — Olist
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.metrics import mean_absolute_error, mean_squared_error


def calcular_metricas(y_real, y_pred, nome_modelo="Modelo"):
    """Calcula e exibe MAE, RMSE e MAPE."""
    mae = mean_absolute_error(y_real, y_pred)
    rmse = np.sqrt(mean_squared_error(y_real, y_pred))
    mape = np.mean(np.abs((y_real - y_pred) / y_real)) * 100

    print(f"\n{'='*40}")
    print(f"  Métricas — {nome_modelo}")
    print(f"{'='*40}")
    print(f"  MAE  : {mae:.2f}")
    print(f"  RMSE : {rmse:.2f}")
    print(f"  MAPE : {mape:.2f}%")
    print(f"{'='*40}\n")

    return {"MAE": mae, "RMSE": rmse, "MAPE": mape}


def plot_serie_temporal(df, coluna_data, coluna_valor, titulo, cor="#2E75B6"):
    """Plota série temporal interativa com Plotly."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df[coluna_data],
        y=df[coluna_valor],
        mode="lines+markers",
        line=dict(color=cor, width=2),
        marker=dict(size=4),
        name=coluna_valor
    ))
    fig.update_layout(
        title=titulo,
        xaxis_title="Data",
        yaxis_title=coluna_valor,
        template="plotly_white",
        hovermode="x unified"
    )
    fig.show()


def criar_features_temporais(df, coluna_data):
    """Adiciona colunas de features temporais a partir de uma coluna de data."""
    df = df.copy()
    df["ano"] = df[coluna_data].dt.year
    df["mes"] = df[coluna_data].dt.month
    df["semana"] = df[coluna_data].dt.isocalendar().week.astype(int)
    df["dia_semana"] = df[coluna_data].dt.dayofweek
    df["trimestre"] = df[coluna_data].dt.quarter
    df["dia_do_ano"] = df[coluna_data].dt.dayofyear
    return df

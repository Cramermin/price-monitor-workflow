# -*- coding: utf-8 -*-
from src.core.workflow import PriceMonitorWorkflow
from src.core.ai_engine import BaseAIEngine

print("\n" + "="*50)
print("🧪 测试价格监控工作流 (无AI增强)")
print("="*50 + "\n")

# 1. 初始化工作流
workflow = PriceMonitorWorkflow()
workflow.set_ai_engine(BaseAIEngine())  # 使用基础AI引擎

# 2. 运行工作流
report = workflow.run_full_workflow()

print("\n" + "="*50)
print("✅ 测试成功完成！")
print("="*50)
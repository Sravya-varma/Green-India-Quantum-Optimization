# Green India: Quantum Computing-Based Environmental Optimization System

## 1. Project Overview
Green India is an environmental data analysis and optimization project. It uses Python to explore pollution data and compares classical budget optimization with a Quantum Approximate Optimization Algorithm (QAOA) experiment.

## 2. Objectives
- Analyze environmental pollution measurements.
- Visualize pollution data using interactive charts.
- Select environmental initiatives under a limited budget.
- Compare classical optimization results with QAOA results.

## 3. Technologies Used
- Python
- Streamlit
- Pandas
- Qiskit
- Qiskit Optimization
- Matplotlib / Streamlit charts

## 4. Environmental Initiatives
The optimization experiment considers:
- Tree Plantation
- Solar Energy
- Waste Management
- Pollution Control
- Water Conservation

## 5. Methodology
1. Load and explore the pollution dataset.
2. Display data using filters, tables, and charts.
3. Define initiative costs, estimated impact scores, and a budget.
4. Find a classical optimization solution.
5. Run a QAOA experiment and compare the results.
6. Display the comparison in the dashboard.

## 6. How to Run
1. Install Python and the required packages.
2. Open the project folder in VS Code.
3. Run `python -m pip install streamlit pandas`.
4. Run `python -m streamlit run app.py`.
5. Open the local URL shown in the terminal.

## 7. Limitations
The initiative costs and impact scores are illustrative values. Pollution concentration measurements are not automatically equivalent to AQI scores. The QAOA experiment does not establish quantum advantage.

## 8. Future Scope
- Calculate AQI using appropriate pollutant-specific standards.
- Use verified environmental cost and impact data.
- Improve optimization experiments and result visualization.
- Expand pollution analysis across regions and time periods.

## Screenshots

### 1. Dashboard Home Page
![Green India Dashboard]("C:\Users\sravy\OneDrive\Documents\green india\screenshots\dashboard home page..png")

### 2. Environmental Data Analysis
![Environmental Data]("C:\Users\sravy\OneDrive\Documents\green india\screenshots\pollution charts.png")

### 3. Classical Optimization
![Classical Optimization]("C:\Users\sravy\OneDrive\Documents\green india\screenshots\filters.png")

### 4. Classical vs Quantum Comparison
![Quantum Comparison]("C:\Users\sravy\OneDrive\Documents\green india\screenshots\classical vs quantum.png")

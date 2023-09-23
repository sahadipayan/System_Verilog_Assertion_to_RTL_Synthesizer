# System_Verilog_Assertion_to_RTL_Synthesizer
A synthesizer capable of transforming SVA properties into synthesizable hardware modules in Verilog register-transfer level (RTL).

# Summary
Assertion-based verification has become a widely accepted validation technique in the pre-silicon SoC design stage. Among available platforms, System Verilog assertion (SVA) is a popular medium for writing assertion-based properties and looking for security vulnerabilities early in the SoC life cycle. However, often such assertions cannot be transferred to the post-silicon validation phase as they cannot be synthesized into hardware description language (HDL) formats. In this project, we develop a synthesizer capable of transforming SVA properties into synthesizable hardware modules in Verilog register-transfer level (RTL). Such HDL realization can be transferred to the post-silicon domain and implemented as hardware monitors to check security properties for validation or in-field operation stage. Our synthesizer tool is developed with maximum scalability to handle complex high-level abstraction properties described in System Verilog into a coherent RTL form with a conditional statement. In this work, we delve deep into the structure of SVA properties and decompose the high-level abstractions into basic communicating parallel hardware units that can operate as a monitor for that property. These synthesized assertions can be used to locate errors, ensuring faster debugging. We verified the synthesized modules with extensive test benches covering all corner case scenarios for functional correctness.

# How to run the tool
Step 1: Open terminal in a folder where all python scripts (parser, RTL generator and GUI scripts) are present 

Step 2: run by following statement  

   “python tool_app2.py” 

Afterwards, a Gui will be opened. 

Step 3: Click “Browse” button to select file to generate synthesized RTL. After selecting the button, a new text box will be appeared that displays the property information. In the same time, synthesized RTL verilogs will be generated in the folder. 

Step 4: Click “Open” button to view generated Verilog module 

# Collaborators
 Dipayan Saha and Md Saad Ull Haque



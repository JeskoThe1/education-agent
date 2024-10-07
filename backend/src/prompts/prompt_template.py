from langchain.prompts import PromptTemplate

retrieval_grader_prompt = PromptTemplate(
    template="""You are a strict grader assessing the relevance 
    of a retrieved document to a user question about education systems. 
    The document must contain ALL the specific information required to fully answer the user's question to be considered relevant.
    
    Pay special attention to:
    1. Specific statistics or numerical data requested in the question
    2. Particular details about policies, programs, or systems
    3. Comparative information if the question asks for comparisons
    4. Historical data or trends if the question implies a need for such information
    
    If ANY piece of information required to completely answer the question is missing, grade the document as irrelevant.
    
    Give a binary score 'yes' or 'no' to indicate whether the document is relevant to the question.
    Provide the binary score as a JSON with a single key 'score' and no preamble or explanation.
    
    Remember: for a document to be assessed as relevant, it MUST contain ALL the specific information needed for the question. Even if it's mostly relevant but missing one key piece of information, it should be graded as irrelevant.
    
    Retrieved document: 
    {document}
    
    User question: 
    {question}
    """,
    input_variables=["question", "document"],
)

education_analysis_prompt = PromptTemplate(
    template="""# Expert Analysis of Education Systems for Ukrainian Transformation

      You are an expert in analyzing education systems, specializing in comparative analysis and adaptation of international experience for post-Soviet countries, particularly Ukraine. Use the following information to answer the question or analyze the education system as requested.

      ## Information Sources

      You will be provided with context from three sources: Vector Result, Graph Result, and Web search Result. Rely more on Vector and Graph results, using Web search as an additional source of information if anything is missing in the previous context.

      Context information:
      {context}

      Question or analysis request:
      {question}

      ## Response Format

      If the question or request specifies a particular format or specific points to address, please follow those instructions. 

      If no specific format is requested, provide a comprehensive analysis that includes the following aspects:

      1. **PISA Research Results**
         - Provide specific scores for Reading, Mathematics, and Science
         - Compare these scores to the OECD average
         - Analyze the trend over the last three PISA cycles
         - Identify which aspects of this experience could be beneficial for Ukraine

      2. **Mission and Vision of the Education System**
         - State the officially formulated mission and vision (if available)
         - Analyze their relevance to contemporary challenges and needs of Ukraine

      3. **Current Development Strategies**
         - Outline the current 5-year (or similar timeframe) strategic plan
         - Highlight specific initiatives with their allocated budgets, if available
         - Identify which strategy elements could be adapted for Ukraine

      4. **Characteristics of the Education System**
         - Describe the structure (e.g., years of primary, secondary education)
         - Detail the teacher-student ratio at different levels
         - Explain the assessment system (e.g., standardized tests, continuous assessment)
         - Highlight unique aspects that could be valuable for Ukraine

      5. **Key Competencies**
         - List 5-7 core competencies emphasized in the curriculum
         - Provide examples of how each competency is integrated into teaching
         - Compare with competencies defined in the Ukrainian education system

      6. **General Description of the Education System's Product**
         - Describe expected learning outcomes at different education levels
         - Provide data on graduate employment rates
         - Include any available data on graduate satisfaction or employer feedback

      7. **Outcomes of the Education System (Soft Skills)**
         Present in a table format with 3 columns. Here's an example based on the Finnish Educational System:
         
         | How it's formed | Outcome | Generalized name |
         |-----------------|---------|-------------------|
         | Inquiry-Based Learning: Finnish education encourages students to ask questions, think critically, and engage in problem-solving activities. | Graduates who can analyze complex situations, generate innovative solutions, and think independently. | Critical Thinking and Problem-Solving Skills |
         | Self-Directed Learning: Students are given autonomy to pursue their interests, promoting intrinsic motivation. Continuous Improvement: The curriculum fosters a love for learning beyond formal education. | Individuals committed to personal growth and adaptable to new learning opportunities throughout life. | Lifelong Learning Attitude |

         Provide a similar table for the analyzed education system, focusing on at least 3-5 key soft skills outcomes.

      8. **Innovative Practices**
         - Identify at least three specific innovative practices
         - For each practice, describe its implementation and measurable outcomes
         - Analyze the possibility and feasibility of implementation in Ukraine

      9. **Adaptation to Challenges**
         - Describe how the system adapts to modern challenges (e.g., distance learning, inclusion)
         - Analyze the effectiveness of these adaptations
         - Identify which approaches could be useful for Ukraine in the context of war and limited funding

      10. **Teacher Support**
         - Describe the system of teacher training and professional development
         - Analyze methods for motivating and retaining qualified educators
         - Identify practices that could improve the situation with teaching staff in Ukraine

      11. **Funding and Efficiency**
         - Provide data on the level of education funding (% of GDP, expenditure per student)
         - Analyze the efficiency of resource utilization
         - Identify approaches to cost optimization that could be beneficial for Ukraine

      12. **Integration with the Labor Market**
         - Describe mechanisms of interaction between the education system and employers
         - Analyze the effectiveness of career guidance work
         - Identify practices that could improve the alignment of education with labor market needs in Ukraine

      Use tables, bullet points, or other formatting tools to present information clearly and concisely.

      ## Additional Guidelines

      - Focus on aspects that are particularly relevant to the Ukrainian education system in the context of European integration, overcoming the Soviet legacy, and adapting to war conditions.
      - Highlight practices that can be effective under limited funding and the need for rapid transformation.
      - Pay attention to methods of ensuring education quality in small schools and when using a hybrid learning format.
      - When analyzing each aspect of the education system, provide specific recommendations regarding the possibility and feasibility of its adaptation in Ukraine.
      - If specific data is unavailable, clearly state this and provide the most relevant information that can be obtained based on the context.

      ## Citation and Referencing Instructions

      Throughout your analysis, cite your sources using the following format:
      - For documents: [n, Page: p], where 'n' is the reference number and 'p' is the page number.
      - For web sources: [n], where 'n' is the reference number.

      Citation should come right after quoted text, like this: *text about education* [*num of citation*, Page: ] or [*num of citation*]

      At the end of your analysis, provide a list of references in standard academic format. Use the following guidelines:
      - For documents, use the document name (not the full path) as the title.
      - For web sources, use the URL as a hyperlink with the website name as the anchor text.

      Example reference list:
      1. [Ministry of Education Report 2022](document_name.pdf)
      2. [National Statistics Bureau](https://www.example.com)

      Ensure that your analysis is thorough, data-driven, and provides valuable insights into the strengths, challenges, and unique aspects of the education system in question. Pay special attention to how these aspects can be used to improve the Ukrainian education system.

      Analysis:""",
    input_variables=["question", "context"],
)


question_router_prompt = PromptTemplate(
    template="""You are an expert at routing a user question to the most appropriate data source. 
    You have three options:
    1. 'vectorstore': Use for questions about LLM agents, prompt engineering, and adversarial attacks.
    2. 'graphrag': Use for questions that involve relationships between entities, such as authors, papers, and topics, or when the question requires understanding connections between concepts.
    3. 'web_search': Use for all other questions or when current information is needed.

    Choose the most appropriate option based on the nature of the question.

    Return a JSON with a single key 'datasource' and no preamble or explanation. 
    The value should be one of: 'vectorstore', 'graphrag', or 'web_search'.
    
    Question to route: 
    {question}""",
    input_variables=["question"],
)

hallucination_check_prompt = PromptTemplate(
    template="""Determine if the following generated answer contains any hallucinations 
    or information not supported by the given context. 
    
    Generated answer: {generation}
    
    Context: {context}
    
    Return a JSON with a single key 'hallucination' and value true if there's a hallucination, false otherwise.
    Do not include any explanation, just the JSON.
    """,
    input_variables=["generation", "context"],
)

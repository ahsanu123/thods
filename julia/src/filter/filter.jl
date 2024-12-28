module Filter

abstract type FilterType end

"""
  Low pass Filter
  rewrite for learning from DSP.jl

  Low pass Filter with Cut off frequiency w
  
"""

struct LowPass{T<:Real} <: FilterType
  w::T

  # constructor
  LowPass{T}(w::Real) where {T<:Real} = new{T}(w)
  LowPass(w::Real) = LowPass{typeof(w / 1)}(w)
end


end

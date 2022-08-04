require_relative 'init.rb'

class Ui
  attr_accessor :props, :component
  def initialize
    @component = []
    @props = { mode: 0, index: 1}
  end

  def render text
    @component.append text 
  end

  def p text
    out = "<p>#{text}</p>" 
    render out
  end
end

